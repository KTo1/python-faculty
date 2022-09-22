import React from "react";


class LoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {username: '', password: ''}
    }

    handleSubmit(event){
        console.log(this.state.username + ', ' + this.state.password)
        this.props.get_token(this.state.username, this.state.password)
        event.preventDefault()
    }

    handleChange(event){
        console.log(event)
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <input type="text" name="username" placeholder="login"
                       value={this.state.username} onChange={(event) => this.handleChange(event)}/>
                <input type="password" name="password" placeholder="password"
                       value={this.state.password} onChange={(event) => this.handleChange(event)}/>
                <input type="submit" value="Login"/>
            </form>
        );
    }

}

export default LoginForm;