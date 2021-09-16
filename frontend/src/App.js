import './App.css';
import React from "react";
import UserList from "./components/Users";
import axios from "axios";
import Header from "./components/Header";
import Footer from "./components/Footer";
import {ProjectList, ProjectDetail} from "./components/Projects";
import ToDoList from "./components/ToDos";
import {Route, Switch, Link, Redirect, BrowserRouter} from "react-router-dom";
import LoginForm from "./components/Auth";

const API_ROOT = "http://127.0.0.1:8000/api";
const getUrl = (name) => `${API_ROOT}${name}`

const pageNotFound = ({location}) => {
    return (
        <h4>'{location.pathname}' page not found :(</h4>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            users: [],
            projects: [],
            project: {},
            todos: [],
            auth: {username: '', isLogged: false}
        };
    }

    login(username, password) {
        axios
            .post(getUrl('/token/'), {username: username, password: password})
            .then(response => {
                const result = response.data
                const access = result.access
                const refresh = result.refresh
                localStorage.setItem('login', username)
                localStorage.setItem('access', access)
                localStorage.setItem('refresh', refresh)
                this.setState({'auth': {username: username, isLogged: true}})
                this.loadData()
            }).catch(error => console.log(error))
    }

    logout() {
        localStorage.setItem('login', '')
        localStorage.setItem('access', '')
        localStorage.setItem('refresh', '')
        this.setState({'auth': {username: '', isLogged: false}})
    }

    getHeaders() {
        let headers = {
            'Content-Type': 'application/json'
        }
        console.log(this.state.auth)
        if (this.state.auth.isLogged) {
            const token = localStorage.getItem('access')
            headers['Authorization'] = 'Bearer' + token
        }
        return headers
    }

    getProject(id) {
        let headers = this.getHeaders();
        axios
            .get(getUrl('/projects/${id}/'), {headers})
            .then(response => {
                this.setState({project: response.data})
            }).catch(error => console.log(error))
    }

    loadData() {
        let headers = this.getHeaders();

        axios
            .get(getUrl('/users/'), {headers})
            .then(response => {
                this.setState({users: response.data.results})
            })
            .catch(error => console.log(error))
        axios
            .get(getUrl('/projects/'), {headers})
            .then(response => {
                this.setState({projects: response.data.results})
            })
            .catch(error => console.log(error))
        axios
            .get(getUrl('/todos/'), {headers})
            .then(response => {
                this.setState({todos: response.data.results})
            })
            .catch(error => console.log(error))
    }

    componentDidMount() {
        const username = localStorage.getItem('login')
        if ((username != "") && (username != null)) {
            this.setState({'auth': {username: username, isLogged: true}}, () => this.loadData())
        }
    }

    render() {
        return (
            <div className="App">
                <Header/>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to={'/'}>Users</Link>
                            </li>
                            <li>
                                <Link to={'/projects'}>Projects</Link>
                            </li>
                            <li>
                                <Link to={'/todos'}>ToDos</Link>
                            </li>
                            <li>
                                <Link to={'/login'}>Login</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todos' component={() => <ToDoList todos={this.state.todos} />} />
                        <Route path='/project/:id'>
                            <ProjectDetail getProject={(id) => this.getProject(id)} item={this.state.projects}/>
                        </Route>
                        <Route exact path='/login'>
                            <LoginForm login={(username, password) => this.login(username, password)}/>
                        </Route>
                        <Redirect from={'/users'} to={'/'}/>
                        <Route component={pageNotFound}/>
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;
