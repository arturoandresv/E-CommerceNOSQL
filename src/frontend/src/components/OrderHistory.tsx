import type { Order } from '../interfaces'

interface OrderHistoryProps {
  readonly orders: Order[]
}

function OrderHistory({ orders }:OrderHistoryProps) {
  return (
    <section>
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-xl font-bold tracking-tight text-on-surface">Order History</h2>
        <button className="text-sm text-primary hover:underline underline-offset-4">View All Activity</button>
      </div>
      <div className="space-y-3">
        {orders.map((order) => (
          <div key={order.order_id} className="grid grid-cols-4 items-center p-6 bg-surface-container-low rounded-xl hover:bg-surface-container transition-all cursor-pointer">
            <div className="flex items-center gap-4">
              <span className="material-symbols-outlined text-on-surface-variant">
                {order.status === "Enviado" ? "local_shipping" : "check_circle"}
              </span>
              <span className="font-bold text-on-surface">ORD#{order.order_id}</span>
            </div>
            <div className="text-on-surface-variant text-sm italic">{order.created_at}</div>
            <div>
              <span className="px-3 py-1 bg-primary/10 text-primary text-[10px] font-bold uppercase tracking-widest rounded-full">
                {order.status}
              </span>
            </div>
            <div className="text-right font-bold text-on-surface">${order.total}</div>
          </div>
        ))}
      </div>
    </section>
  )
}

export default OrderHistory