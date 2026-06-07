/**
 * Anime Analytics — Shared JS Utilities
 * Chart defaults, API helpers, formatting functions
 */

// ── API BASE ──────────────────────────────────────────────────────────────────
const API = {
  base: window.location.origin,

  async get(endpoint, params = {}) {
    const url = new URL(`${this.base}/api/${endpoint}`);
    Object.entries(params).forEach(([k, v]) => v && url.searchParams.set(k, v));
    const res = await fetch(url);
    if (!res.ok) throw new Error(`API error: ${res.status}`);
    return res.json();
  },

  async post(endpoint, body = {}) {
    const res = await fetch(`${this.base}/api/${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
    if (!res.ok) throw new Error(`API error: ${res.status}`);
    return res.json();
  }
};

// ── FORMAT HELPERS ────────────────────────────────────────────────────────────
const fmt = {
  money:   (v) => v >= 1000 ? `$${(v/1000).toFixed(1)}B` : `$${v.toFixed(0)}M`,
  moneyFull: (v) => `$${v.toFixed(1)}M`,
  score:   (v) => (+v).toFixed(2),
  pct:     (v) => `${(+v).toFixed(1)}%`,
  ratio:   (v) => `${(+v).toFixed(1)}×`,
  num:     (v) => Number(v).toLocaleString(),
};

// ── CHART DEFAULTS ────────────────────────────────────────────────────────────
const COLORS = {
  cyan:    '#00f5ff',
  magenta: '#ff00aa',
  gold:    '#ffd700',
  green:   '#00ff88',
  red:     '#ff3366',
  violet:  '#aa44ff',
  orange:  '#ff8800',
  teal:    '#00ddaa',
  pink:    '#ff66cc',
  blue:    '#4488ff',
  palette: [
    '#00f5ff','#ff00aa','#ffd700','#00ff88','#ff3366',
    '#aa44ff','#ff8800','#00ddaa','#ff66cc','#4488ff',
    '#ffaa00','#cc00ff','#00ffcc','#ff4488'
  ]
};

function chartDefaults(Chart) {
  Chart.defaults.color = 'rgba(232, 244, 255, 0.55)';
  Chart.defaults.font.family = "'Exo 2', sans-serif";
  Chart.defaults.font.size = 12;
  Chart.defaults.borderColor = 'rgba(0, 245, 255, 0.08)';

  // Global plugin defaults
  Chart.defaults.plugins.legend.labels.usePointStyle = true;
  Chart.defaults.plugins.legend.labels.pointStyle = 'circle';
  Chart.defaults.plugins.legend.labels.padding = 16;
  Chart.defaults.plugins.tooltip.backgroundColor = 'rgba(7, 11, 26, 0.95)';
  Chart.defaults.plugins.tooltip.borderColor = 'rgba(0, 245, 255, 0.3)';
  Chart.defaults.plugins.tooltip.borderWidth = 1;
  Chart.defaults.plugins.tooltip.padding = 12;
  Chart.defaults.plugins.tooltip.cornerRadius = 8;
  Chart.defaults.plugins.tooltip.titleColor = '#00f5ff';
  Chart.defaults.plugins.tooltip.bodyColor = 'rgba(232, 244, 255, 0.85)';
}

// ── GRADIENT HELPERS ─────────────────────────────────────────────────────────
function makeGradient(ctx, from, to, vertical = true) {
  const grad = vertical
    ? ctx.createLinearGradient(0, 0, 0, ctx.canvas.height)
    : ctx.createLinearGradient(0, 0, ctx.canvas.width, 0);
  grad.addColorStop(0, from);
  grad.addColorStop(1, to);
  return grad;
}

// ── TOAST ─────────────────────────────────────────────────────────────────────
function toast(msg, dur = 3000) {
  let el = document.getElementById('toast');
  if (!el) {
    el = document.createElement('div');
    el.id = 'toast';
    document.body.appendChild(el);
  }
  el.textContent = msg;
  el.classList.add('show');
  setTimeout(() => el.classList.remove('show'), dur);
}

// ── NAV ACTIVE ────────────────────────────────────────────────────────────────
function setNavActive() {
  const path = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === path);
  });
}
document.addEventListener('DOMContentLoaded', setNavActive);

// ── ANIMATE ON SCROLL ─────────────────────────────────────────────────────────
function observeCards() {
  const obs = new IntersectionObserver(
    (entries) => entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.opacity = '1';
        e.target.style.transform = 'translateY(0)';
      }
    }),
    { threshold: 0.08 }
  );
  document.querySelectorAll('.card, .kpi-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    obs.observe(el);
  });
}
document.addEventListener('DOMContentLoaded', observeCards);

// ── RENDER NAV ────────────────────────────────────────────────────────────────
function renderNav() {
  const navHtml = `
  <nav>
    <a href="/" class="nav-logo">
      <span class="logo-text">ANIME<span class="logo-accent">X</span></span>
    </a>
    <ul class="nav-links">
      <li><a href="/">Home</a></li>
      <li><a href="/dashboard">Dashboard</a></li>
      <li><a href="/insights">Insights</a></li>
      <li><a href="/predict">Predict</a></li>
    </ul>
  </nav>`;
  const target = document.getElementById('nav-placeholder');
  if (target) target.outerHTML = navHtml;
}
document.addEventListener('DOMContentLoaded', renderNav);
