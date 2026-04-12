import type { Order, OrderItem } from '../interfaces'

interface OrderDetailProps {
  readonly order: Order | null
  readonly items: OrderItem[]
}

function OrderDetail({ order, items }: OrderDetailProps) {
  if (!order) return null

  return (
    <section className="bg-surface-container-low rounded-xl overflow-hidden">
      <div className="p-8 border-b border-outline-variant/10 flex justify-between items-end">
        <div>
          <div className="flex items-center gap-3 mb-2">
            <h1 className="text-3xl font-extrabold tracking-tighter text-on-surface">
              ORD#{order.order_id}
            </h1>
            <span className="px-3 py-1 bg-tertiary/10 text-tertiary text-[10px] font-bold uppercase tracking-widest rounded-full">
              {order.status}
            </span>
          </div>
          <p className="text-on-surface-variant text-sm">Processed on {order.created_at}</p>
        </div>
        <div className="text-right">
          <p className="text-[10px] uppercase tracking-[0.2em] text-on-surface-variant">Total Amount</p>
          <p className="text-4xl font-light text-primary">${order.total.toFixed(2)}</p>
        </div>
      </div>

      <div className="p-8 space-y-6">
        {items.map((item) => (
          <div key={item.item_id} className="flex items-center gap-6">
            <div className="w-24 h-24 bg-surface-container-highest rounded-xl flex items-center justify-center flex-shrink-0">
              <span className="material-symbols-outlined text-on-surface-variant text-4xl">inventory_2</span>
            </div>
            <div className="flex-grow">
              <div className="flex justify-between items-start">
                <div>
                  <h3 className="text-lg font-medium text-on-surface">{item.product_name}</h3>
                </div>
                <p className="text-lg font-semibold text-on-surface">${item.unit_price.toFixed(2)}</p>
              </div>
              <p className="mt-2 text-xs text-on-surface-variant">Quantity: {item.quantity}</p>
            </div>
          </div>
        ))}
      </div>

      <div className="bg-surface-variant/30 p-8 flex justify-between items-center">
        <div className="flex gap-4">
          <button className="px-6 py-2 rounded-lg bg-surface-container-high text-on-surface text-sm font-bold hover:bg-surface-bright transition-colors">
            Track Shipment
          </button>
          <button className="px-6 py-2 rounded-lg border border-outline-variant/30 text-on-surface-variant text-sm hover:border-outline transition-colors">
            Download Invoice
          </button>
        </div>
        <p className="text-xs text-on-surface-variant italic">Shipping to: {order.shipping_address}</p>
      </div>
    </section>
  )
}

export default OrderDetail