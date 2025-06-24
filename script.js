document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault(); // Evita el envío real del formulario

  const nombre = document.getElementById("nombre").value.trim();
  const motivo = document.getElementById("motivo").value.trim();
  const correo = document.getElementById("correo").value.trim();
  const mensaje = document.getElementById("mensaje");

  if (!nombre || !motivo || !correo) {
    mensaje.style.color = "red";
    mensaje.textContent = "Por favor, completa todos los campos.";
    return;
  }

  const emailRegex = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
  if (!emailRegex.test(correo)) {
    mensaje.style.color = "red";
    mensaje.textContent = "Ingresa un correo electrónico válido.";
    return;
  }

  mensaje.style.color = "green";
  mensaje.textContent = `¡Gracias por contactarnos, ${nombre}! Nos comunicaremos pronto.`;

  this.reset(); // Limpia el formulario
});
