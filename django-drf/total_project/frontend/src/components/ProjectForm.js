import React from "react";


class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {name: '', repo: '', users: []}
    }

    handleSubmit(event){
        console.log(this.state.name + ', ' + this.state.repo + ', ' + this.state.users)
        this.props.create_proc(this.state.name, this.state.repo, this.state.users)
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

    handleUserChange(event){
        if(!event.target.selectedOptions){
            this.setState({'users': []})
            return
        }

        let users = []
        for(let i=0;i<event.target.selectedOptions.length;i++){
            users.push(event.target.selectedOptions.item(i).value)
        }

        this.setState({'users': users})
        console.log(this.state)
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <input type="text" name="name" placeholder="name"
                       value={this.state.name} onChange={(event) => this.handleChange(event)}/>

                <input type="text" name="repo" placeholder="repo"
                       value={this.state.repo} onChange={(event) => this.handleChange(event)}/>

                <select name="users" multiple onChange={(event) => this.handleUserChange(event)}>
                    {this.props.users.map((item)=><option value={item.id}>{item.username}</option>)}
                </select>

                <input type="submit" value="Save"/>
            </form>
        );
    }

}

export default ProjectForm;