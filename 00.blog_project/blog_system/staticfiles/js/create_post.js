function submitForm(ev) {
    const formData = new FormData(this);

        fetch('/api/blogs/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': Cookies.get('csrftoken'),
            },
            body: JSON.stringify({
                title: formData.get('title'),
                text: formData.get('text'),
                blog_id: formData.get('blog_id'),
            })
        })
            .then(response => response.json())
            .then(json => console.log(json))
            .catch(err => console.log(err))
    ev.preventDefault()
    return false;

    }

document.querySelector('#form-create-post')
    .addEventListener('submit', submitForm);


