// Toggle sidebar visibility on smaller screens
const sidebar = document.getElementById("sidebar");
const sidebarToggle = document.getElementById("sidebarToggle");
const closeSidebar = document.getElementById("closeSidebar");

// Open sidebar
sidebarToggle.addEventListener("click", () => {
  sidebar.classList.toggle("hidden");
});

// Close sidebar
closeSidebar.addEventListener("click", () => {
  sidebar.classList.add("hidden");
});
