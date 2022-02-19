
function searchName(){
    let username = document.getElementById('usernameQuery').value;
    let nameAndUsername = document.getElementById('nameAndUsername')
    let errorMsg = document.getElementById('errorMsg')

    if (!username){
        errorMsg.innerHTML = 'Please enter valid username.'
        nameAndUsername.innerHTML = ''
    }else{
        let url = `http://127.0.0.1:3000/api/members?username=${username}`;
        fetch(url)
        .then((res) => 
            res.json()
        )
        .then((jsonData) => {

            if(jsonData.data === null){
                errorMsg.innerHTML = 'User not found.'
                nameAndUsername.innerHTML = ''
            }
            else{
                let name = jsonData.data.name
                if(name === undefined){
                errorMsg.innerHTML = 'User not found.'
                nameAndUsername.innerHTML = ''
            }else{
                nameAndUsername.innerHTML = name + '(' + username + ')';
                errorMsg.innerHTML = ''
            }}})
        .catch((err) => 
        console.log('ERROR:', err)
        )
    }
    
}

function updateName() {
    let updateName = document.getElementById('nameToUpdate').value
    fetch("http://127.0.0.1:3000/api/member", {
      method:'POST',
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ "name": updateName })
    })
    .then(res => res.json())
    .then(result => {
        console.log(result)
        if (result.ok === true) {
          document.getElementById('updateStatus').innerHTML = '更新成功';
          document.getElementById('welcome-msg').innerHTML = `${updateName}，歡迎登入系統`
        } else if(result.error == true) {
          document.getElementById('updateStatus').innerHTML = '更新失敗';
        }
      })
      .catch(err => console.log('Error: '+ err))
  }

const toSearch = document.getElementById('search-btn')
toSearch.addEventListener('click',searchName)

const toUpdate = document.getElementById('update-btn')
toUpdate.addEventListener('click',updateName)

