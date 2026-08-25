const fallbackApiBaseUrl = 'http://127.0.0.1:8000';

export const API_BASE_URL = (import.meta.env.PUBLIC_API_URL || fallbackApiBaseUrl).replace(/\/$/, '');
