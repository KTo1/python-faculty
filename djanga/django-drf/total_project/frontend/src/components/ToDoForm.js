import React from "react";


class ToDoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {project: props.projects[0], subject: '', user: ''}
    }

    handleSubmit(event){
        console.log(this.state.project + ', ' + this.state.subject + ', ' + this.state.user)
        this.props.create_proc(this.state.project, this.state.subject, this.state.user)
        event.preventDefault()
    }

    handleChange(event){
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
        console.log(this.state)
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.projects.length && nextProps.users.length) {
            this.setState({project: nextProps.projects[0].id, subject: '', user: nextProps.users[0].id})
        }
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <select name="project" onChange={(event) => this.handleChange(event)}>
                    {this.props.projects.map((item)=><option value={item.id}>{item.name}</option>)}
                </select>

                <input type="text" name="subject" placeholder="subject"
                       value={this.state.subject} onChange={(event) => this.handleChange(event)}/>

                <select name="user" onChange={(event) => this.handleChange(event)}>
                    {this.props.users.map((item)=><option value={item.id}>{item.username}</option>)}
                </select>

                <input type="submit" value="Save"/>
            </form>
        );
    }

}

export default ToDoForm;