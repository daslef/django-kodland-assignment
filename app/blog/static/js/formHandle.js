const file = document.querySelector('input[type="file"]');
const form = document.querySelector('form');

file.addEventListener('change', e => {

    const uploadWrapper = document.createElement('div')
    const image = document.createElement('img') 
    const closeBtn = document.createElement('a')

    image.src = URL.createObjectURL(event.target.files[0])
    image.classList.add('form__uploaded')

    closeBtn.innerHTML = `
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="12" cy="12" r="12" fill="#E5E5E5"/>
        <line x1="16.9498" y1="7.05025" x2="7.05029" y2="16.9497" stroke="white" stroke-width="2"/>
        <line x1="16.9496" y1="16.9498" x2="7.05014" y2="7.05029" stroke="white" stroke-width="2"/>
        </svg>`
    closeBtn.classList.add('form__button-close')

    closeBtn.addEventListener('click', function() {
        image.remove()
        this.remove()
        const file = document.createElement('input')
        file.setAttribute('type', 'file')
        file.setAttribute('name', 'image')
        file.setAttribute('accept', 'image/*')
        file.setAttribute('id', 'id_image')
        form.querySelector('p:nth-child(4)').appendChild(uploadWrapper)
    })
    
    uploadWrapper.appendChild(image)
    uploadWrapper.appendChild(closeBtn)

    form.querySelector('p:nth-child(4)').appendChild(uploadWrapper)
    // file.remove()
})