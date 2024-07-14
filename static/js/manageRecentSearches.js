const current = JSON.parse(localStorage.getItem("searches"));

const recentSearches = document.getElementById("recent-searches");
const searchCityButton = document.getElementById("search-city");

if (!current) {
  recentSearches.innerHTML = "<p>No recent searches</p>";
} else {
  recentSearches.innerHTML = current
    .map((search) => "<p>" + search + "</p>")
    .join(" ");
}

searchCityButton.addEventListener("click", updateLocalStorage);

function updateLocalStorage() {
  const newEntry = document.getElementById("location").value;
  if (!newEntry) {
    return;
  }
  let current = JSON.parse(localStorage.getItem("searches"));
  console.log(current, newEntry);
  if (current && current.length >= 5) {
    current.pop();
  }
  if (current) {
    current.unshift(newEntry);
  } else {
    current = [newEntry];
  }
  localStorage.setItem("searches", JSON.stringify(current));
  recentSearches.innerHTML = current
    .map((search) => "<p>" + search + "</p>")
    .join(" ");
}
