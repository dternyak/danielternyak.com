import React, { Component } from 'react';
import 'bootstrap-webpack';

/* global styles for app */
import 'style!./styles/app.scss';

/* application components */
import { Header } from 'components/Header';

export class App extends Component {
    static propTypes = {
        children: React.PropTypes.any,
    }

    render() {
        return (
            <section>
                <Header />
                {this.props.children}
            </section>
        );
    }
}
