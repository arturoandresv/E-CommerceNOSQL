const BASE_URL = "http://localhost:8000"

export const api = {
  getUser: (userId: string) =>
    fetch(`${BASE_URL}/users/${userId}`).then(res => res.json()),

  getOrdersByUser: (userId: string) =>
    fetch(`${BASE_URL}/users/${userId}/orders`).then(res => res.json()),

  getAddresses: (userId: string) =>
    fetch(`${BASE_URL}/users/${userId}/addresses`).then(res => res.json()),

  getPaymentMethods: (userId: string) =>
    fetch(`${BASE_URL}/users/${userId}/payment-methods`).then(res => res.json()),

  getOrderDetail: (orderId: string) =>
    fetch(`${BASE_URL}/orders/${orderId}`).then(res => res.json()),

  getItemsByOrder: (orderId: string) =>
    fetch(`${BASE_URL}/orders/${orderId}/items`).then(res => res.json()),
}