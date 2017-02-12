import React, { Component } from 'react';
import DocumentMeta from 'react-document-meta';

/* components */
import {EachPost} from '../../components/EachPost';
import { connect } from 'react-redux';

@connect(
    state => {
        return {state: state}
    }
)
export class EachPostView extends Component {


    render() {
        return (
            <section>
                <EachPost id={this.props.params.id} />
            </section>
        );
    }
}
