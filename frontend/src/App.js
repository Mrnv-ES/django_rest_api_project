import './App.css';
import React from "react";
import UserList from "./components/Users";
import axios from "axios";
import Header from "./components/Header";
import Footer from "./components/Footer"
import ProjectItem from "./components/ProjectItem";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDos";
import {HashRouter, Route, Switch, Link, Redirect, BrowserRouter} from "react-router-dom";

const API_ROOT = "http://127.0.0.1:8000/api/";
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
            'users': [],
            'projects': [],
            'todos': []
        };
    }

    componentDidMount() {
            axios
                .get(getUrl('users'))
                .then(response => {
                    const users = response.data
                    this.setState (
                        {
                            'users': users.results
                        }
                    )
                })
                .catch(error => console.log(error))
            axios
                .get(getUrl('projects'))
                .then(response => {
                    const projects = response.data
                    this.setState (
                        {
                            'projects': projects.results
                        }
                    )
                })
                .catch(error => console.log(error))
            axios
                .get(getUrl('todos'))
                .then(response => {
                    const todos = response.data
                    this.setState (
                        {
                            'todos': todos.results
                        }
                    )
                })
                .catch(error => console.log(error))
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
                                <Link to={'/projects/'}>Projects</Link>
                            </li>
                            <li>
                                <Link to={'/todos/'}>ToDos</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                        <Route exact path='/projects/' component={() => <ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todos/' component={() => <ToDoList todos={this.state.todos} />} />
                        <Route path='/project/:id'>
                            <ProjectItem projects={this.state.projects} />
                        </Route>
                        <Redirect from={'/users/'} to={'/'}/>
                        <Route component={pageNotFound}/>
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;
