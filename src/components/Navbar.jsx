export default function Navbar() {
  return (
    <header className="navbar">
      <div className="logo">MetaCraft<span>AI</span></div>
      <nav>
        <a href="#features">Features</a>
        <a href="#pricing">Pricing</a>
        <a href="#faq">FAQ</a>
        <button className="btn-outline">Sign In</button>
      </nav>
    </header>
  );
}
