import logo from './logo.svg';
import './App.css';
import React from "react";
import axios from "axios";

import UserList from './components/Users';
import ProjectList from "./components/Projects";
import ProjectTodoList from "./components/ProjectTodo";
import ProjectForm from "./components/ProjectForm";
import ProjectSearchForm from "./components/ProjectSearchForm";
import TodoList from "./components/ToDoS";
import ToDoForm from "./components/ToDoForm";
import Menu from "./components/Menu";
import Footer from "./components/Footer";
import NotFound404 from "./components/NotFound404";
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie";


import {HashRouter, BrowserRouter, Routes, Route, Navigate, Link} from "react-router-dom";


class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': '',
            'address':'127.0.0.1:8000'
        }
    }

    create_todo(project, subject, user) {
        const headers = this.get_headers()
        const data = {project: project, subject: subject, user: user}

        axios.post(`http://${this.state.address}/api/todos/`, data, {headers}).then(response => {
            this.load_data();
        }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }

    delete_todo(id) {
        const headers = this.get_headers()

        axios.delete(`http://${this.state.address}api/todos/${id}`, {headers}).then(response => {
            this.load_data();
        }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }

    create_project(name, repo, users) {
        const headers = this.get_headers()
        const data = {name: name, repo: repo, users: users}

        axios.post(`http://${this.state.address}/api/projects/`, data, {headers}).then(response => {
            this.load_data();
        }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }

    delete_project(id) {
        const headers = this.get_headers()

        axios.delete(`http://${this.state.address}/api/projects/${id}`, {headers}).then(response => {
            this.load_data();
        }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }

    search_project(name) {
        const headers = this.get_headers()

        axios.get(`http://${this.state.address}/api/projects/?name=${name}`, {headers}).then(response => {
            this.setState(
                {
                    'projects': response.data['results']
                })
        }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }

    is_auth() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookie = new Cookies;
        const token = cookie.get('token');
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post(`http://${this.state.address}/api-token-auth/`, {username: username, password: password}).then(response => {
            console.log(response.data)
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль!'))
    }

    set_token(token) {
        const cookie = new Cookies;
        cookie.set('token', token);
        this.setState({'token': token}, () => this.load_data())
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }

        return headers;
    }

    load_data() {

        const headers = this.get_headers()

        axios.get(`http://${this.state.address}/api/users/`, {headers}).then(response => {
            this.setState(
                {
                    'users': response.data['results']
                })
        }).catch(error => console.log(error))

        axios.get(`http://${this.state.address}/api/projects/`, {headers}).then(response => {
            this.setState(
                {
                    'projects': response.data['results']
                })
        }).catch(error => console.log(error))

        axios.get(`http://${this.state.address}/api/todos/`, {headers}).then(response => {
            this.setState(
                {
                    'todos': response.data['results']
                })
        }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage();
        this.load_data();
    }

    render() {
        return (
            <div>
                <Menu menu/>

                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link as={Link} to='/'> Projects </Link></li>
                            <li><Link as={Link} to='/todos'> Todos </Link></li>
                            <li><Link as={Link} to='/users'> Users </Link></li>
                            <li> {this.is_auth() ? <button
                                    onClick={() => this.logout()}>Logout</button> :
                                <Link as={Link} to='/login'>Login</Link>}</li>
                        </ul>
                    </nav>

                    <Routes>
                        <Route exact path='/' element={<Navigate to='/projects'/>}/>
                        <Route exact path='/todos/' element={<TodoList items={this.state.todos}
                                                                       delete_proc={(id) => this.delete_todo(id)}/>}/>
                        <Route exact path='/todos/create/' element={<ToDoForm projects={this.state.projects} users={this.state.users}
                                                                             create_proc={(project, subject, user) => this.create_todo(project, subject, user)}/>}/>
                        <Route exact path='/users/' element={<UserList items={this.state.users}/>}/>
                        <Route exact path='/login/' element={<LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>

                        <Route path='/projects'>
                            <Route index element={<ProjectList items={this.state.projects} delete_proc={(id) => this.delete_project(id)}/>}/>
                            <Route path='project/:projectId' element={<ProjectTodoList items={this.state.todos}/>}/>
                            <Route exact path='/projects/create/' element={<ProjectForm users={this.state.users}
                                                     create_proc={(name, repo, users) => this.create_project(name, repo, users)}/>}/>
                            <Route exact path='/projects/search/' element={<ProjectSearchForm projects={this.state.projects}
                                                     search_proc={(name) => this.search_project(name)}/>}/>

                        </Route>

                        <Route path='*' element={NotFound404}/>
                    </Routes>
                </BrowserRouter>
                <Footer footer/>
            </div>
        )
    }
}

export default App;
