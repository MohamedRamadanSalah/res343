/**
 * Shared Firebase Firestore REST Client
 * Used by both index.html (read) and admin/index.html (read+write)
 */
class FirebaseClient {
  constructor(config) {
    this.apiKey = config.apiKey;
    this.projectId = config.projectId;
    this.authDomain = config.authDomain;
    this.baseUrl = `https://firestore.googleapis.com/v1/projects/${config.projectId}/databases/(default)/documents`;
    this.authToken = null;
  }

  setAuthToken(token) {
    this.authToken = token;
  }

  // ── HTTP helper ─────────────────────────────────────────────
  async _request(endpoint, options = {}) {
    const sep = endpoint.includes('?') ? '&' : '?';
    const url = `${this.baseUrl}${endpoint}${sep}key=${this.apiKey}`;
    const headers = { 'Content-Type': 'application/json' };
    if (this.authToken) {
      headers['Authorization'] = `Bearer ${this.authToken}`;
    }
    const res = await fetch(url, { headers, ...options });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.error?.message || `HTTP ${res.status}`);
    }
    // Firestore DELETE returns 200 with empty body — handle safely
    const text = await res.text();
    if (!text || text.trim() === '') return null;
    return JSON.parse(text);
  }

  // ── CRUD ─────────────────────────────────────────────────────
  async getAll(collection) {
    const data = await this._request(`/${collection}?pageSize=500`);
    return (data && data.documents ? data.documents : []).map(d => this._toObj(d));
  }

  async getDoc(collection, id) {
    const data = await this._request(`/${collection}/${id}`);
    return this._toObj(data);
  }

  async create(collection, obj, id = null) {
    const docId = id || `doc_${Date.now()}_${Math.random().toString(36).slice(2, 9)}`;
    const body = { fields: this._toFields(obj) };
    // Use separate URL so documentId is never mixed with key param
    const url = `${this.baseUrl}/${collection}?documentId=${encodeURIComponent(docId)}&key=${this.apiKey}`;
    const headers = { 'Content-Type': 'application/json' };
    if (this.authToken) {
      headers['Authorization'] = `Bearer ${this.authToken}`;
    }
    const res = await fetch(url, { method: 'POST', headers, body: JSON.stringify(body) });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.error?.message || `HTTP ${res.status}`);
    }
    const text = await res.text();
    return this._toObj(text ? JSON.parse(text) : null);
  }

  async update(collection, id, obj) {
    // PATCH without updateMask = replace entire document (safe since we send all fields)
    const body = { fields: this._toFields(obj) };
    const data = await this._request(`/${collection}/${id}`, {
      method: 'PATCH', body: JSON.stringify(body)
    });
    return this._toObj(data);
  }

  async delete(collection, id) {
    await this._request(`/${collection}/${id}`, { method: 'DELETE' });
    return true;
  }

  // ── Firestore type conversions ──────────────────────────────────
  _toObj(doc) {
    if (!doc || !doc.fields) return null;
    const obj = {};
    for (const [k, v] of Object.entries(doc.fields)) obj[k] = this._fromField(v);
    if (doc.name) {
      // Strip any query string that may have been accidentally embedded in old doc IDs
      obj.id = doc.name.split('/').pop().split('?')[0];
    }
    return obj;
  }

  _fromField(f) {
    if (f.stringValue  !== undefined) return f.stringValue;
    if (f.integerValue !== undefined) return parseInt(f.integerValue);
    if (f.doubleValue  !== undefined) return parseFloat(f.doubleValue);
    if (f.booleanValue !== undefined) return f.booleanValue;
    if (f.nullValue    !== undefined) return null;
    if (f.arrayValue)  return (f.arrayValue.values || []).map(v => this._fromField(v));
    if (f.mapValue)    {
      const o = {};
      for (const [k, v] of Object.entries(f.mapValue.fields || {})) o[k] = this._fromField(v);
      return o;
    }
    return null;
  }

  _toFields(obj) {
    const f = {};
    for (const [k, v] of Object.entries(obj)) f[k] = this._toField(v);
    return f;
  }

  _toField(v) {
    if (v === null || v === undefined) return { nullValue: null };
    if (typeof v === 'string')  return { stringValue: v };
    if (typeof v === 'boolean') return { booleanValue: v };
    if (typeof v === 'number')  return Number.isInteger(v) ? { integerValue: String(v) } : { doubleValue: v };
    if (Array.isArray(v))       return { arrayValue: { values: v.map(i => this._toField(i)) } };
    if (typeof v === 'object')  return { mapValue: { fields: this._toFields(v) } };
    return { stringValue: String(v) };
  }
}

// ── Firebase Authentication (REST) ─────────────────────────────
class FirebaseAuth {
  constructor(config) {
    this.apiKey = config.apiKey;
    this.signInUrl = `https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=${config.apiKey}`;
    this.user = null;
    this._listeners = [];
  }

  async signIn(email, password) {
    const res = await fetch(this.signInUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password, returnSecureToken: true })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error?.message || 'Login failed');
    this.user = { email: data.email, uid: data.localId, token: data.idToken, refreshToken: data.refreshToken };
    sessionStorage.setItem('fbUser', JSON.stringify(this.user));
    this._notify();
    return this.user;
  }

  signOut() {
    this.user = null;
    sessionStorage.removeItem('fbUser');
    this._notify();
  }

  restoreSession() {
    const saved = sessionStorage.getItem('fbUser');
    if (saved) {
      this.user = JSON.parse(saved);
      this._notify();
    }
    return this.user;
  }

  onAuthChange(fn) { this._listeners.push(fn); }
  _notify() { this._listeners.forEach(fn => fn(this.user)); }
}

window.FirebaseClient = FirebaseClient;
window.FirebaseAuth = FirebaseAuth;
