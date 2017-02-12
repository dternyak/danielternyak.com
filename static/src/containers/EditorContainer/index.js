import React, { Component } from 'react';
import DocumentMeta from 'react-document-meta';

/* components */
import {Editor} from '../../components/Editor';


export class EditorContainer extends Component {
    render() {
        return (
            <section>
                <Editor/>
            </section>

        );
    }
}
