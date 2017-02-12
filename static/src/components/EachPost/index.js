import React, { Component } from 'react';

import {get_single_post} from '../../utils/http_functions'

export class EachPost extends Component {

    constructor(props) {
        super(props);
        this.state = {
            post: [],
            loading: true
        }
    }

    componentDidMount() {
        setTimeout(() => {
            get_single_post(this.props.id)
                .then((response) => {
                        response.data.data.body = {__html: response.data.data.body};
                        this.setState({
                            post: response.data.data,
                            loading: false
                        })
                    }
                );
        }, 500);

    }

    render() {
        const post = this.state.post;
        return (
            <div>
                {this.state.loading ? <div className="loader">Loading...</div> :
                    <div className="container" style={{"marginTop": -50, "marginBottom": 50}}>
                        <div className="row">
                            <div className="col-lg-8">
                                <h1><b>{post.title}</b></h1>

                                <p className="lead">
                                    by: {post.author}
                                </p>
                                <hr/>
                                <p> Posted on {post.time} </p>
                                <hr/>
                                <div dangerouslySetInnerHTML={post.body}></div>
                            </div>
                        </div>


                    </div>
                }
            </div >



        )
    }

}
