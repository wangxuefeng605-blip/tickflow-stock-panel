export class ApiError extends Error {
  status: number;
  detail?: unknown;

  constructor(
    message: string,
    status: number,
    detail?: unknown,
  ) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.detail = detail;
  }
}

async function request<T>(
  method: string,
  url: string,
  body?: unknown,
): Promise<T> {
  const response = await fetch(url, {
    method,
    headers: {
      "Content-Type": "application/json",
    },
    body: body === undefined
      ? undefined
      : JSON.stringify(body),
  });

  const contentType =
    response.headers.get("content-type") ?? "";

  const data = contentType.includes("application/json")
    ? await response.json()
    : await response.text();

  if (!response.ok) {
    throw new ApiError(
      `API request failed: ${response.status}`,
      response.status,
      data,
    );
  }

  return data as T;
}

export const api = {
  get<T>(url: string) {
    return request<T>("GET", url);
  },

  post<T>(url: string, body?: unknown) {
    return request<T>("POST", url, body);
  },

  put<T>(url: string, body?: unknown) {
    return request<T>("PUT", url, body);
  },

  delete<T>(url: string) {
    return request<T>("DELETE", url);
  },
};