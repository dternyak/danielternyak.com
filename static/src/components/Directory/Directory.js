import React, { Component, PropTypes } from 'react'
import { Link } from 'react-router';

class Directory extends Component {
    render() {
        const resume_url = "https://drive.google.com/file/d/0B3hYpsXRDCIkRUV4UTJlbXNMYTA/view?usp=sharing"
        return (
            <div id="h">
                <div className="container centered">
                    <div className="row">
                        <div className="col-md-8 col-md-offset-2">
                            <h1>Hello, my name is <b>Daniel Ternyak</b>.<br/>I create web applications with
                                <b> Python</b> and <b>JavaScript</b> on the <b>Cloud.</b></h1>
                        </div>
                    </div>
                    <div className="row mt">
                        <div className="col-sm-4">

                            <i className="ion-monitor"/>
                            <Link to="/portfolio" activeClassName="active">

                                <h3><b>Portfolio</b></h3>
                            </Link>
                        </div>

                        <div className="col-sm-4">
                            <i className="ion-ios-bookmarks-outline"/>
                            <Link to="/blog" activeClassName="active">
                            <h3><b>Blog</b></h3>
                                </Link>
                        </div>

                        <div className="col-sm-4">
                            <i className="ion-ios-paper-outline"/>
                            <a target="_blank" href={resume_url}>

                                <h3><b>Rèsumè</b></h3>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}


export default Directory