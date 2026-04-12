export interface User {
  user_id: string
  name: string
  email: string
}

export interface Address {
  address_id: string
  user_id: string
  street: string
  city: string
}

export interface PaymentMethod {
  payment_id: string
  user_id: string
  type: string
  last_four: string | null
}

export interface Order {
  order_id: string
  user_id: string
  status: string
  total: number
  created_at: string
  shipping_address: string
}

export interface OrderItem {
  item_id: string
  order_id: string
  product_name: string
  quantity: number
  unit_price: number
  subtotal: number
}