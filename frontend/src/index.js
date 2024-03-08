const axios = require('axios')

// fetch - courses data
// axios - students data

async function getStudents(){
    let result = await axios.get('http://127.0.0.1:8000/user/list/')

    let data = result.data;

    console.log(data)
}

async function getCourses(){
    const response = await fetch('http://127.0.0.1:8000/course/list/')
    const response_data = await response.text()
    console.log(response_data)
}

getCourses()

getStudents()