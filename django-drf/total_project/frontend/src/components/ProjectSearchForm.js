import React from "react";


class ProjectSearchForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {name: ''}
    }

    handleSubmit(event){
        console.log(this.state.name)
        this.props.search_proc(this.state.name)
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

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <input type="text" name="name" placeholder="name"
                       value={this.state.name} onChange={(event) => this.handleChange(event)}/>

                <input type="submit" value="Search"/>

                <div>
                    <table>
                        <th>
                            Id
                        </th>
                        <th>
                            Name
                        </th>
                        {this.props.projects.map((item)=> <tr><td>{item.id}</td><td>{item.name}</td></tr>)}
                    </table>

                </div>
            </form>
        );
    }

}

export default ProjectSearchForm;