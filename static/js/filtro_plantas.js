const aplicacion = document.querySelector(".container")

const url = "https://perenual.com/api/species-list?key=sk-yl4e6521da2899f312380&page=3"

fetch(url)
.then(res => res.json())
.then(data => {
    data.forEach( plantas => {
        console.log(plantas.common_name)
    })
    /*console.log(data)*/
})
.catch(err => console.log(err))