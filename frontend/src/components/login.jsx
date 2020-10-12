import React, { Component } from "react";

class Login extends Component{
    constructor(prop){
        super(prop);
        this.state = {username: "", password: ""};

        this.handleChage = this.handleChage.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChage(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    handleSubmit(event) {
        alert('A username and password was submitted: ' + this.state.username + " " + this.state.password);
        event.preventDefault();
    }

    render() {
        return (
            <div>Login
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Username:
                        <input name="username" type="text" value={this.state.username} onChange={this.handleChage}/>
                    </label>
                    <lable>
                        Password:
                        <input name="password" type="password" value={this.state.password} onChange={this.handleChage}/>
                    </lable>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        )
    }
}
export default Login;