
function searchPlants() {
    // Get the search term from the input field
    let searchTerm = document.getElementById('searchInput').value;

    // Display the loader (optional)
    document.getElementById('loader').style.display = 'block';

    // Perform an AJAX request
    fetch(`/flora/search-plants/?q=${encodeURIComponent(searchTerm)}`)
        .then(response => response.json())
        .then(data => {
            // Hide the loader
            document.getElementById('loader').style.display = 'none';

            // Get the table body where results will be displayed
            let plantTableBody = document.getElementById('plantTableBody');

            // Clear previous results
            plantTableBody.innerHTML = '';

            // Loop through the data and add rows to the table
            data.plants.forEach(plant => {
                let row = `<tr>
                    <td>${plant.name}</td>
                    <td>${plant.discoverer_first_name}</td>
                </tr>`;
                plantTableBody.innerHTML += row;
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            document.getElementById('loader').style.display = 'none';
        });
}