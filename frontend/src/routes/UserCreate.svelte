<script>
    import { push } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"

    let error = {detail:[]}
    let username = ''
    let password1 = ''
    let password2 = ''
    let email = ''
    
    function post_user(event) {
        event.preventDefault()
        let url = "/api/user/create"
        let params = {
            username: username,
            password1: password1,
            password2: password2,
            email: email,
        }
        fastapi('post', url, params, 
            (json) => {
                push("/user-login")
            },
            (json_error) => {
                error = json_error
            }
        )
    }
</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">회원 등록</h5>
    <Error error={error} />
    <form method="post" class="my-3">
        <div class="mb-3">
            <label for="username">사용자이름</label>
            <input type="text" class="form-control" bind:value="{username}">
        </div>
        <div class="mb-3">
            <label for="password1">비밀번호</label>
            <input type="password" class="form-control" bind:value="{password1}">
        </div>
        <div class="mb-3">
            <label for="password2">비밀번호 확인</label>
            <input type="password" class="form-control" bind:value="{password2}">
        </div>
        <div class="mb-3">
            <label for="email">이메일</label>
            <input type="text" class="form-control" bind:value="{email}">
        </div>
        <button class="btn btn-primary" on:click="{post_user}">등록하기</button>
    </form>
</div>