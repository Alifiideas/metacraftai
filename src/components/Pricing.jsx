export default function Pricing() {
  return (
    <section id="pricing" className="pricing">
      <h2>Choose your pricing plan</h2>

      <div className="pricing-grid">

        <div className="card bronze">
          <h3>Bronze</h3>
          <h1>$3</h1>
          <p>5,000 images</p>
        </div>

        <div className="card silver popular">
          <h3>Silver</h3>
          <h1>$5</h1>
          <p>9,000 images</p>
        </div>

        <div className="card gold">
          <h3>Gold</h3>
          <h1>$8</h1>
          <p>15,000 images</p>
        </div>

      </div>
    </section>
  );
}
