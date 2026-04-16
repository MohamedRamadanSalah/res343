// Firebase REST API Client - No CDN needed!
class FirebaseAPI {
  constructor(config) {
    this.apiKey = config.apiKey;
    this.projectId = config.projectId;
    this.baseUrl = `https://firestore.googleapis.com/v1/projects/${config.projectId}/databases/(default)/documents`;
  }

  // Helper: Handle fetch requests
  async request(endpoint, options = {}) {
    const url = `${this.baseUrl}${endpoint}?key=${this.apiKey}`;
    try {
      const response = await fetch(url, {
        headers: { "Content-Type": "application/json" },
        ...options,
      });
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error?.message || "API Error");
      }
      return await response.json();
    } catch (error) {
      console.error("Firebase API Error:", error);
      throw error;
    }
  }

  // Get all documents from a collection
  async getAll(collection) {
    try {
      const data = await this.request(`/${collection}`);
      return (data.documents || []).map((doc) => this.docToObject(doc));
    } catch (error) {
      console.error(`Error getting ${collection}:`, error);
      return [];
    }
  }

  // Get single document
  async getDoc(collection, docId) {
    try {
      const data = await this.request(`/${collection}/${docId}`);
      return this.docToObject(data);
    } catch (error) {
      console.error(`Error getting ${collection}/${docId}:`, error);
      return null;
    }
  }

  // Create document
  async createDoc(collection, data) {
    try {
      const body = {
        fields: this.objectToFields(data),
      };
      const response = await this.request(`/${collection}?documentId=${Date.now()}`, {
        method: "POST",
        body: JSON.stringify(body),
      });
      return this.docToObject(response);
    } catch (error) {
      console.error(`Error creating ${collection}:`, error);
      throw error;
    }
  }

  // Update document
  async updateDoc(collection, docId, data) {
    try {
      const body = {
        fields: this.objectToFields(data),
      };
      const response = await this.request(`/${collection}/${docId}`, {
        method: "PATCH",
        body: JSON.stringify(body),
      });
      return this.docToObject(response);
    } catch (error) {
      console.error(`Error updating ${collection}/${docId}:`, error);
      throw error;
    }
  }

  // Delete document
  async deleteDoc(collection, docId) {
    try {
      await this.request(`/${collection}/${docId}`, {
        method: "DELETE",
      });
      return true;
    } catch (error) {
      console.error(`Error deleting ${collection}/${docId}:`, error);
      throw error;
    }
  }

  // Convert Firestore document to JavaScript object
  docToObject(doc) {
    if (!doc || !doc.fields) return null;
    const obj = {};
    for (const [key, value] of Object.entries(doc.fields)) {
      obj[key] = this.fieldToValue(value);
    }
    // Extract ID from document name
    if (doc.name) {
      obj.id = doc.name.split("/").pop();
    }
    return obj;
  }

  // Convert Firestore field types to JavaScript values
  fieldToValue(field) {
    if (field.stringValue !== undefined) return field.stringValue;
    if (field.integerValue !== undefined) return parseInt(field.integerValue);
    if (field.doubleValue !== undefined) return parseFloat(field.doubleValue);
    if (field.booleanValue !== undefined) return field.booleanValue;
    if (field.timestampValue !== undefined) return new Date(field.timestampValue);
    if (field.arrayValue) {
      return (field.arrayValue.values || []).map((v) => this.fieldToValue(v));
    }
    if (field.mapValue) {
      const obj = {};
      for (const [key, value] of Object.entries(field.mapValue.fields || {})) {
        obj[key] = this.fieldToValue(value);
      }
      return obj;
    }
    return null;
  }

  // Convert JavaScript object to Firestore field format
  objectToFields(obj) {
    const fields = {};
    for (const [key, value] of Object.entries(obj)) {
      fields[key] = this.valueToField(value);
    }
    return fields;
  }

  // Convert JavaScript value to Firestore field format
  valueToField(value) {
    if (typeof value === "string") {
      return { stringValue: value };
    }
    if (typeof value === "number") {
      if (Number.isInteger(value)) {
        return { integerValue: value.toString() };
      }
      return { doubleValue: value };
    }
    if (typeof value === "boolean") {
      return { booleanValue: value };
    }
    if (value instanceof Date) {
      return { timestampValue: value.toISOString() };
    }
    if (Array.isArray(value)) {
      return {
        arrayValue: {
          values: value.map((v) => this.valueToField(v)),
        },
      };
    }
    if (typeof value === "object" && value !== null) {
      return {
        mapValue: {
          fields: this.objectToFields(value),
        },
      };
    }
    return { stringValue: "" };
  }
}

// Export globally
window.FirebaseAPI = FirebaseAPI;
