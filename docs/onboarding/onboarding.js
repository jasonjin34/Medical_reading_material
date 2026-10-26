// Onboarding figures: click a .xobs figure to enlarge it, click again or press Esc to close.
document.addEventListener("click", (e) => {
  const fig = e.target.closest(".xobs");
  if (!fig || !e.target.closest(".xo-scroll")) return;
  const open = fig.classList.toggle("xo-open");
  document.body.classList.toggle("xo-lock", open);
});
document.addEventListener("keydown", (e) => {
  if (e.key !== "Escape") return;
  document.querySelectorAll(".xobs.xo-open").forEach((f) => f.classList.remove("xo-open"));
  document.body.classList.remove("xo-lock");
});
