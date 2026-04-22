import type { User, Address, PaymentMethod } from '../interfaces'

interface UserProfileProps {
  readonly user: User | null
  readonly addresses: Address[]
  readonly paymentMethods: PaymentMethod[]
}

export const UserProfile = ({ user, addresses, paymentMethods }: UserProfileProps) => {
  return (
    <div className="col-span-12 lg:col-span-4 space-y-8">
      <section className="bg-surface-container-low p-8 rounded-xl">
        <h2 className="text-xs font-bold tracking-[0.2em] text-primary uppercase mb-6">Profile Identity</h2>
        <div className="space-y-6">
          <div>
            <label className="text-[10px] uppercase tracking-widest text-on-surface-variant block mb-1">Full Name</label>
            <p className="text-xl font-light text-on-surface">{user?.name}</p>
          </div>
          <div>
            <label className="text-[10px] uppercase tracking-widest text-on-surface-variant block mb-1">Primary Email</label>
            <p className="text-lg font-light text-on-surface">{user?.email}</p>
          </div>
        </div>
      </section>

      <section className="bg-surface-container rounded-xl p-8">
        <h2 className="text-xs font-bold tracking-[0.2em] text-primary uppercase mb-6">Saved Destinations</h2>
        <div className="space-y-4">
          {addresses.map((addr) => (
            <div key={addr.address_id} className="flex items-center gap-4 p-4 bg-surface-container-high rounded-lg hover:bg-surface-bright transition-colors cursor-pointer">
              <span className="material-symbols-outlined text-tertiary">location_on</span>
              <div>
                <p className="text-sm font-semibold text-on-surface">{addr.city}</p>
                <p className="text-xs text-on-surface-variant">{addr.street}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="bg-surface-container rounded-xl p-8">
        <h2 className="text-xs font-bold tracking-[0.2em] text-primary uppercase mb-6">Financial Assets</h2>
        <div className="space-y-4">
          {paymentMethods.map((pm) => (
            <div key={pm.payment_id} className="flex items-center justify-between p-4 bg-surface-container-high rounded-lg">
              <div className="flex items-center gap-4">
                <span className="material-symbols-outlined text-on-surface">
                  {pm.type === "Visa" ? "credit_card" : "account_balance_wallet"}
                </span>
                <p className="text-sm text-on-surface">
                  {pm.type} {pm.last_four ? `•••• ${pm.last_four}` : ""}
                </p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  )
}

export default UserProfile