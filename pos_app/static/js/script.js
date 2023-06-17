document.addEventListener('DOMContentLoaded', function(){
    var tabLinks = document.getElementsByClassName("magriza")
    var commonForm = document.getElementById("commonForm")

    commonForm.addEventListener('submit', function(e){
        // e.preventDefault()

        const formData = new FormData(commonForm)

    })

    for (var i=0; i < tabLinks.length; i++){
        tabLinks[i].addEventListener('click', function(){
            let currentActive = document.querySelector(".active")

            if(currentActive){
                currentActive.classList.remove('active')
            }
            this.classList.add("active");

            fetch("{% url 'category-change' %}",{
                method:'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}'
                  },
                body: JSON.stringify({ common: "Solomon"})
            }).then(function(response){
                if (response.ok){
                    window.location.reload();
                }
            })

            
        })
    }
})