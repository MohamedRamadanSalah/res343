// Firebase REST API wrapper - works without CDN
class FirebaseREST {
  constructor(config) {
    this.apiKey = config.apiKey;
    this.projectId = config.projectId;
    this.baseUrl = `https://firestore.googleapis.com/v1/projects/${config.projectId}/databases/(default)/documents`;
  }

  // Read from Firestore using REST API
  async read(collection, docId = null) {
    try {
      if (docId) {
        // Get single document
        const url = `${this.baseUrl}/${collection}/${docId}?key=${this.apiKey}`;
        const response = await fetch(url);
        if (!response.ok) return null;
        return await response.json();
      } else {
        // List all documents in collection
        const url = `${this.baseUrl}/${collection}?key=${this.apiKey}`;
        const response = await fetch(url);
        if (!response.ok) return [];
        const data = await response.json();
        return data.documents || [];
      }
    } catch (error) {
      console.error("Firebase REST read error:", error);
      return docId ? null : [];
    }
  }

  // Convert Firestore REST response to plain JavaScript object
  docToObject(doc) {
    if (!doc || !doc.fields) return null;
    const obj = {};
    for (const [key, value] of Object.entries(doc.fields)) {
      obj[key] = this.fieldToValue(value);
    }
    obj.id = doc.name.split("/").pop();
    return obj;
  }

  // Convert Firestore field types to JavaScript values
  fieldToValue(field) {
    if (field.stringValue) return field.stringValue;
    if (field.numberValue) return parseFloat(field.numberValue);
    if (field.booleanValue) return field.booleanValue;
    if (field.arrayValue) 
      return (field.arrayValue.values || []).map(v => this.fieldToValue(v));
    if (field.mapValue) {
      const obj = {};
      for (const [key, value] of Object.entries(field.mapValue.fields || {})) {
        obj[key] = this.fieldToValue(value);
      }
      return obj;
    }
    if (field.timestampValue) return new Date(field.timestampValue);
    return null;
  }
}

// Export for use in HTML
window.FirebaseREST = FirebaseREST;
