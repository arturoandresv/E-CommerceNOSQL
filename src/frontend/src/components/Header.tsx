import type { User } from '../interfaces'

interface HeaderProps {
  readonly user: User | null
}

export const Header = ({ user }: HeaderProps) => {
  return (
    <header className="fixed top-0 right-0 w-[calc(100%-16rem)] z-40 bg-[#060e20]/60 backdrop-blur-xl flex justify-between items-center px-8 h-20">
      <div className="flex items-center w-1/2">
        <div className="relative w-full max-w-md">
          <span className="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-on-surface-variant">
            search
          </span>
          <input
            type="text"
            placeholder="Search curated orders..."
            className="w-full bg-surface-container-low border-none rounded-xl pl-12 pr-4 py-2 text-on-surface focus:ring-2 focus:ring-primary placeholder:text-on-surface-variant/50"
          />
        </div>
      </div>

      <div className="flex items-center gap-6">
        <button className="relative text-on-surface-variant hover:text-on-surface transition-opacity">
          <span className="material-symbols-outlined">notifications</span>
          <span className="absolute top-0 right-0 w-2 h-2 bg-error rounded-full"></span>
        </button>
        <button className="text-on-surface-variant hover:text-on-surface transition-opacity">
          <span className="material-symbols-outlined">shopping_bag</span>
        </button>
        <div className="flex items-center gap-3 pl-4 border-l border-outline-variant/20">
          <div className="text-right">
            <p className="text-sm font-bold text-on-surface">{user?.name}</p>
            <p className="text-[10px] text-on-surface-variant">{user?.email}</p>
          </div>
          <div className="w-10 h-10 rounded-full bg-surface-container-high flex items-center justify-center">
            <span className="material-symbols-outlined text-primary">person</span>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header