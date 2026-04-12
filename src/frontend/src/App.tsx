import { useEffect, useState } from 'react'
import Sidebar from './components/Sidebar'
import Header from './components/Header'
import UserProfile from './components/UserProfile'
import OrderDetail from './components/OrderDetail'
import OrderHistory from './components/OrderHistory'
import { api } from './services/api'
import type { User, Address, PaymentMethod, Order, OrderItem } from './interfaces'

function App() {
  const USER_ID = "1"
  const ORDER_ID = "555"

  const [user, setUser] = useState<User | null>(null)
  const [addresses, setAddresses] = useState<Address[]>([])
  const [paymentMethods, setPaymentMethods] = useState<PaymentMethod[]>([])
  const [orderDetail, setOrderDetail] = useState<Order | null>(null)
  const [orderItems, setOrderItems] = useState<OrderItem[]>([])
  const [orderHistory, setOrderHistory] = useState<Order[]>([])

  useEffect(() => {
    api.getUser(USER_ID).then(setUser)
    api.getAddresses(USER_ID).then(setAddresses)
    api.getPaymentMethods(USER_ID).then(setPaymentMethods)
    api.getOrderDetail(ORDER_ID).then(setOrderDetail)
    api.getItemsByOrder(ORDER_ID).then(setOrderItems)
    api.getOrdersByUser(USER_ID).then(setOrderHistory)
  }, [])

  return (
    <div className="dark">
      <Sidebar />
      <Header user={user} />
      <main className="ml-64 pt-20 p-8 min-h-screen">
        <div className="grid grid-cols-12 gap-8">
          <UserProfile user={user} addresses={addresses} paymentMethods={paymentMethods} />
          <div className="col-span-12 lg:col-span-8 space-y-8">
            <OrderDetail order={orderDetail} items={orderItems} />
            <OrderHistory orders={orderHistory} />
          </div>
        </div>
      </main>
    </div>
  )
}

export default App