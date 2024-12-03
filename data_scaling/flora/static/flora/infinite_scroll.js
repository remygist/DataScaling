document.addEventListener("DOMContentLoaded", function () {
    let offset = 0;
    const limit = 25;
    const loadingMessage = document.getElementById("loading-message");
    const plantTable = document.getElementById("plant-table");
    let isLoading = false;
    let hasMoreData = true;

    async function loadMorePlants() {
        if (isLoading || !hasMoreData) return;

        isLoading = true;
        if (loadingMessage) loadingMessage.style.display = "block";

        try {
            const response = await fetch(`/flora/infinite-scroll-data/?offset=${offset}&limit=${limit}`);
            if (!response.ok) throw new Error("Failed to fetch more plants.");

            const data = await response.json();

            data.plants.forEach(plant => {
                const row = document.createElement("tr");
                row.innerHTML = `<td>${plant.name}</td><td>${plant.discoverer}</td>`;
                plantTable.appendChild(row);
            });

            hasMoreData = data.has_more;
            offset += limit;

        } catch (error) {
            console.error("Error loading plants:", error);
        } finally {
            if (loadingMessage) loadingMessage.style.display = "none";
            isLoading = false;
        }
    }

    function handleScroll() {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 200) {
            loadMorePlants();
        }
    }

    window.addEventListener("scroll", handleScroll);
    loadMorePlants();
});
