import React, { Component } from 'react';
import DocumentMeta from 'react-document-meta';
import { connect } from 'react-redux';

/* components */
import Portfolio from '../../components/Portfolio/Portfolio';
@connect(
    state => {
        return  {state: state}
    }
)
export class PortfolioView extends Component {
    render() {
        return (
            <section>
                <Portfolio/>
            </section>
        );
    }
}
