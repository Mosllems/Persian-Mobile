// نوار کشویی مانند منو در حالت ریسپانسیو
const navToggleIcon = document.querySelector('.nav__toggle-icon')
const menu = document.querySelector('.menu')
//سبدخرید
const navBtn = document.querySelector(".nav__btn")
const navMenu = document.querySelector(".nav-menu")
const closeBtn = document.querySelector(".close-btn")
let navOpen = false
let navClose = true
//خرید هوشمندانه
const cleverlyListItems = document.querySelectorAll('.cleverly-list__item')
//خرید پرفروش
const bestsellerListItems = document.querySelectorAll('.bestseller-list__item')

navToggleIcon.addEventListener('click',function (){
    this.classList.toggle('nav__toggle-icon--open')
    menu.classList.toggle('menu--open')
})

navBtn.addEventListener("click",function(){
    if(navOpen){
        navBtn.classList.remove("nav-btn--open")
        navMenu.classList.remove("nav-menu--open")
        navOpen = false
    }
    else{
        navBtn.classList.add("nav-btn--open")
        navMenu.classList.add("nav-menu--open")
        navOpen = true
    }
})
closeBtn.addEventListener("click",function(){
    if(navClose){
        navBtn.classList.remove("nav-btn--open")
        navMenu.classList.remove("nav-menu--open")
        navClose = true
    }
    else{
        navBtn.classList.remove("nav-btn--open")
        navMenu.classList.remove("nav-menu--open")
        navClose = false
    }
})

cleverlyListItems.forEach(cleverlyListItem => {
    cleverlyListItem.addEventListener('click',function (){
        document.querySelector('.cleverly-list__item--active').classList.remove('cleverly-list__item--active')
        document.querySelector('.cleverly-content--show').classList.remove('cleverly-content--show')
        this.classList.add('cleverly-list__item--active')
        let contentId = this.getAttribute('data-content-id')
        document.querySelector(contentId).classList.add('cleverly-content--show')
    })
})


bestsellerListItems.forEach(bestsellerListItem => {
    bestsellerListItem.addEventListener('click',function (){
        document.querySelector('.bestseller-list__item--active').classList.remove('bestseller-list__item--active')
        document.querySelector('.bestseller-content--show').classList.remove('bestseller-content--show')
        this.classList.add('bestseller-list__item--active')
        let contentId = this.getAttribute('data-content-id')
        document.querySelector(contentId).classList.add('bestseller-content--show')
    })
})