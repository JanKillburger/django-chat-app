const chatlist = document.querySelector('#chatlist');
  const chatlistWrapper = document.querySelector('.chatlist-wrapper');
  document
    .getElementById('message-form')
    .addEventListener('submit', sendMessage);
  chatlistWrapper.scrollTop = 1_000_000;

  function sendMessage(ev) {
    ev.preventDefault();
    messageEl = document.getElementById('message');
    if (messageEl.value) {
      let fd = new FormData();
      fd.append('message', messageEl.value);
      fd.append('csrfmiddlewaretoken', csrfToken);
      fetch('/chat/', {
        method: 'post',
        body: fd,
      })
        .then((res) => {
          if (res.status === 200) {
            addMessage();
          }
        })
        .catch((err) => console.error(err));
    }
  }

  function addMessage() {
    const currentDate = new Date().toLocaleDateString("de-DE", {year: "2-digit", month: "2-digit", day: "2-digit"});
    const message = document.createElement('li');
    const date = document.createElement('span');
    date.textContent = currentDate + ' ';
    message.appendChild(date);
    const username = document.createElement('span');
    username.textContent = userName + ': ';
    message.appendChild(username);
    const text = document.createElement('span');
    text.textContent = messageEl.value;
    message.appendChild(text);
    chatlist.appendChild(message);
    messageEl.value = '';
  }