document.addEventListener('DOMContentLoaded', () => { document.querySelectorAll('.message').forEach((message) => { setTimeout(() => message.remove(), 4000); }); });
