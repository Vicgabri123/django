document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const tableRows = document.querySelectorAll('tbody tr');

    searchInput.addEventListener('input', function() {
        const filter = searchInput.value.toLowerCase();

        tableRows.forEach(row => {
            const cells = row.getElementsByTagName('td');
            let rowContainsText = false;

            for (let cell of cells) {
                if (cell.textContent.toLowerCase().includes(filter)) {
                    rowContainsText = true;
                    break;
                }
            }

            row.style.display = rowContainsText ? '' : 'none';
        });
    });
});

function teste(){
    alert("Botão funcionou");
}