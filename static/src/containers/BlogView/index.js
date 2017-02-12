import React, { Component } from 'react';
import DocumentMeta from 'react-document-meta';
import { connect } from 'react-redux';

/* components */
import {YourPosts} from '../../components/YourPosts';

@connect(
    state => {
        return {state: state}
    }
)
export class BlogView extends Component {
    render() {
        return (
            <section>
                <YourPosts/>
            </section>
        );
    }
}
