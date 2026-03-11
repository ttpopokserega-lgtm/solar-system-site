// створюємо сцену
const scene = new THREE.Scene()

// -----------------------------
// СТВОРЕННЯ ЗІРОК
// -----------------------------

const starsGeometry = new THREE.BufferGeometry()

const starsCount = 10000
const positions = []

for(let i=0;i<starsCount;i++){

positions.push((Math.random()-0.5)*1000)
positions.push((Math.random()-0.5)*1000)
positions.push((Math.random()-0.5)*1000)

}

starsGeometry.setAttribute(
'position',
new THREE.Float32BufferAttribute(positions,3)
)

const starsMaterial = new THREE.PointsMaterial({
color:0xffffff,
size:0.7
})

const stars = new THREE.Points(starsGeometry,starsMaterial)

scene.add(stars)


// -----------------------------
// КАМЕРА
// -----------------------------

const camera = new THREE.PerspectiveCamera(
75,
window.innerWidth/window.innerHeight,
0.1,
1000
)

camera.position.z = 40


// -----------------------------
// РЕНДЕР
// -----------------------------

const renderer = new THREE.WebGLRenderer({antialias:true})

renderer.setSize(window.innerWidth, window.innerHeight)

document.body.appendChild(renderer.domElement)


// -----------------------------
// КЕРУВАННЯ КАМЕРОЮ
// -----------------------------

const controls = new THREE.OrbitControls(camera, renderer.domElement)


// -----------------------------
// СВІТЛО
// -----------------------------

const light = new THREE.PointLight(0xffffff,2)

scene.add(light)


// -----------------------------
// СОНЦЕ
// -----------------------------

const sunGeometry = new THREE.SphereGeometry(4,32,32)

const sunMaterial = new THREE.MeshBasicMaterial({
color:0xffff00
})

const sun = new THREE.Mesh(sunGeometry,sunMaterial)

scene.add(sun)


// -----------------------------
// ФУНКЦІЯ СТВОРЕННЯ ПЛАНЕТ
// -----------------------------

function createPlanet(size,color,distance){

const geometry = new THREE.SphereGeometry(size,32,32)

const material = new THREE.MeshStandardMaterial({color:color})

const planet = new THREE.Mesh(geometry,material)

planet.position.x = distance

// орбіта планети
const orbitGeometry = new THREE.RingGeometry(distance-0.05,distance+0.05,64)

const orbitMaterial = new THREE.MeshBasicMaterial({
color:0xffffff,
side:THREE.DoubleSide
})

const orbit = new THREE.Mesh(orbitGeometry,orbitMaterial)

orbit.rotation.x = Math.PI/2

scene.add(orbit)

scene.add(planet)

return planet

}


// -----------------------------
// СТВОРЮЄМО ПЛАНЕТИ
// -----------------------------

const mercury = createPlanet(0.5,0xaaaaaa,6)
const venus = createPlanet(0.9,0xffcc88,9)
const earth = createPlanet(1,0x2233ff,12)
const mars = createPlanet(0.8,0xff3300,15)
const jupiter = createPlanet(2.5,0xffaa88,20)
const saturn = createPlanet(2,0xffddaa,26)
const uranus = createPlanet(1.5,0x66ffff,32)
const neptune = createPlanet(1.4,0x3366ff,38)


// -----------------------------
// ЧАС ДЛЯ ОРБІТ
// -----------------------------

let t = 0


// -----------------------------
// АНІМАЦІЯ
// -----------------------------

function animate(){

requestAnimationFrame(animate)

t += 0.01


// орбіти планет

mercury.position.x = Math.cos(t*4)*6
mercury.position.z = Math.sin(t*4)*6

venus.position.x = Math.cos(t*3)*9
venus.position.z = Math.sin(t*3)*9

earth.position.x = Math.cos(t*2)*12
earth.position.z = Math.sin(t*2)*12

mars.position.x = Math.cos(t*1.6)*15
mars.position.z = Math.sin(t*1.6)*15

jupiter.position.x = Math.cos(t*0.8)*20
jupiter.position.z = Math.sin(t*0.8)*20

saturn.position.x = Math.cos(t*0.6)*26
saturn.position.z = Math.sin(t*0.6)*26

uranus.position.x = Math.cos(t*0.4)*32
uranus.position.z = Math.sin(t*0.4)*32

neptune.position.x = Math.cos(t*0.3)*38
neptune.position.z = Math.sin(t*0.3)*38


// обертання планет навколо осі

mercury.rotation.y += 0.02
venus.rotation.y += 0.01
earth.rotation.y += 0.03
mars.rotation.y += 0.02
jupiter.rotation.y += 0.04
saturn.rotation.y += 0.03
uranus.rotation.y += 0.02
neptune.rotation.y += 0.02


// легкий рух зірок

stars.rotation.y += 0.0005


renderer.render(scene,camera)

}

animate()


// -----------------------------
// РЕАКЦІЯ НА ЗМІНУ РОЗМІРУ ВІКНА
// -----------------------------

window.addEventListener("resize", () => {

camera.aspect = window.innerWidth / window.innerHeight

camera.updateProjectionMatrix()

renderer.setSize(window.innerWidth, window.innerHeight)

})