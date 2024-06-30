
$(document).ready(function() {
    $('.candidat').click(function(e) {
        e.preventDefault();
        
        var candidatId = $(this).data('candidat-id');
        console.log(candidatId);
        
        $.ajax({
            type: 'POST',
            url: "{% url 'vote' %}",
            data: {
                'candidatId': candidatId,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function(response) {
                // Mettez à jour l'affichage ou effectuez d'autres actions en cas de succès
                console.log(response); // Exemple: afficher la réponse dans la console
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText); // Gestion des erreurs
            }
        });
    });
});