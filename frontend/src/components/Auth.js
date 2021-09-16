import React from "react";

class LoginForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {login: '', password: ''}
    }

    handlerOnChange(event) {
        this.setState({[event.target.name]: event.target.value})
    }

    handlerOnSubmit(event) {
        this.props.login(this.state.login, this.state.password)
        event.preventDefault()
    }

    render(){
        return (
            <form onSubmit={(event) => this.handlerOnSubmit(event)}>
                <div className="form-group">
                    <label for="username">Username</label>
                    <input type="text" className="form-control" name="login" value={this.state.login}
                           onChange={(event) => this.handlerOnChange(event)}/>
                </div>
                <div className="form-group">
                    <label for="password">Password</label>
                    <input type="password" className="form-control" name="password" value={this.state.password}
                           onChange={(event) => this.handlerOnChange(event)}/>
                </div>
                <input type="submit" className="btn" value="Login"/>
            </form>
        )
    }
}

export default LoginForm;
