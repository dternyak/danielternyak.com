import React, { Component } from 'react';
import { Link } from 'react-router';


export class Header extends Component {
    constructor(props) {
        super(props);
    }


    render() {
        return (
            <header ref="header">
                <nav className="navbar navbar-default" role="navigation">
                <div className="navbar-header">
                    <button type="button" className="navbar-toggle" data-toggle="collapse"
                            data-target=".navbar-collapse">
                        <span className="sr-only">Toggle navigation</span>
                        <span className="icon-bar"/>
                        <span className="icon-bar"/>
                        <span className="icon-bar"/>
                    </button>

                    <div className="logo">
                        <Link to="/home" activeClassName="active">
                            <h2>DT</h2>
                        </Link>
                    </div>
                </div>
                <div className="collapse navbar-collapse">

                    <ul className="nav navbar-nav pull-right">

                        <li><a target="_blank" href="https://github.com/dternyak"><i
                            className="ion-social-github"/> GitHub</a></li>

                        <li><a target="_blank" href="https://www.linkedin.com/profile/view?id=421754785&trk=hp-identity-photo"><i
                            className="ion-social-linkedin"/> LinkedIn</a></li>


                    </ul>
                </div>
                </nav>
            </header>
        );
    }
}

