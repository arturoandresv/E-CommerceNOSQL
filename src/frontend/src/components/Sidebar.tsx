export const Sidebar = () => {
  return (
    <nav className="bg-[#060e20] h-screen w-64 fixed left-0 top-0 flex flex-col py-8 z-50">
      
      {/* Logo */}
      <div className="px-8 mb-12">
        <span className="text-2xl font-bold tracking-tighter text-[#dee5ff]">
          Editorial Noir
        </span>
        <p className="text-on-surface-variant text-xs mt-1">Premium Curator</p>
      </div>

      {/* Navigation Links */}
      <div className="flex-grow flex flex-col gap-2">
        <a href="#" className="flex items-center gap-4 px-8 py-4 text-[#a3aac4] hover:text-[#dee5ff] hover:bg-[#141f38] transition-colors duration-200">
          <span className="material-symbols-outlined">dashboard</span>
          <span>Overview</span>
        </a>
        <a href="#" className="flex items-center gap-4 px-8 py-4 text-[#8eabff] font-bold border-r-2 border-[#8eabff] bg-[#141f38]">
          <span className="material-symbols-outlined">shopping_cart</span>
          <span>Orders</span>
        </a>
        <a href="#" className="flex items-center gap-4 px-8 py-4 text-[#a3aac4] hover:text-[#dee5ff] hover:bg-[#141f38] transition-colors duration-200">
          <span className="material-symbols-outlined">person</span>
          <span>Profile</span>
        </a>
        <a href="#" className="flex items-center gap-4 px-8 py-4 text-[#a3aac4] hover:text-[#dee5ff] hover:bg-[#141f38] transition-colors duration-200">
          <span className="material-symbols-outlined">settings</span>
          <span>Settings</span>
        </a>
      </div>

      {/* Button */}
      <div className="px-6 mt-auto">
        <button className="w-full py-3 rounded-full bg-primary text-on-primary font-bold text-xs uppercase tracking-widest">
          New Collection
        </button>
      </div>

    </nav>
  )
}

export default Sidebar