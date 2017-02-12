import React, { Component } from 'react';
import {create_post, is_admin} from '../../utils/http_functions'


export class Editor extends Component {

    constructor(props) {
        super(props);
        this.state = {
            content: null,
            title: null,
            loading: true
        }
    }

    editorConfig() {
        return (
            <div>
                <h2>Editor</h2>
                <div className="toolbar">
                    <span className="ql-format-group">
                    <select title="Font" className="ql-font">
                        <option value="sans-serif">Sans Serif</option>
                        <option value="serif">Serif</option>
                        <option value="monospace">Monospace</option>
                    </select>
                    <select title="Size" className="ql-size">
                        <option value="10px">Small</option>
                        <option value="13px">Normal</option>
                        <option value="18px">Large</option>
                        <option value="32px">Huge</option>
                    </select>
                    </span>
                    <span className="ql-format-group">
                    <span title="Bold" className="ql-format-button ql-bold"/>
                    <span className="ql-format-separator"/>
                    <span title="Italic" className="ql-format-button ql-italic"/>
                    <span className="ql-format-separator"/>
                    <span title="Underline" className="ql-format-button ql-underline"/>
                    <span className="ql-format-separator"/>
                    <span title="Strikethrough" className="ql-format-button ql-strike"/>
                    </span>
                    <span className="ql-format-group">
                    <select title="Text Color" className="ql-color">
                        <option value="rgb(0, 0, 0)" label="rgb(0, 0, 0)"/>
                        <option value="rgb(230, 0, 0)" label="rgb(230, 0, 0)"/>
                        <option value="rgb(255, 153, 0)" label="rgb(255, 153, 0)"/>
                        <option value="rgb(255, 255, 0)" label="rgb(255, 255, 0)"/>
                        <option value="rgb(0, 138, 0)" label="rgb(0, 138, 0)"/>
                        <option value="rgb(0, 102, 204)" label="rgb(0, 102, 204)"/>
                        <option value="rgb(153, 51, 255)" label="rgb(153, 51, 255)"/>
                        <option value="rgb(255, 255, 255)" label="rgb(255, 255, 255)"/>
                        <option value="rgb(250, 204, 204)" label="rgb(250, 204, 204)"/>
                        <option value="rgb(255, 235, 204)" label="rgb(255, 235, 204)"/>
                        <option value="rgb(255, 255, 204)" label="rgb(255, 255, 204)"/>
                        <option value="rgb(204, 232, 204)" label="rgb(204, 232, 204)"/>
                        <option value="rgb(204, 224, 245)" label="rgb(204, 224, 245)"/>
                        <option value="rgb(235, 214, 255)" label="rgb(235, 214, 255)"/>
                        <option value="rgb(187, 187, 187)" label="rgb(187, 187, 187)"/>
                        <option value="rgb(240, 102, 102)" label="rgb(240, 102, 102)"/>
                        <option value="rgb(255, 194, 102)" label="rgb(255, 194, 102)"/>
                        <option value="rgb(255, 255, 102)" label="rgb(255, 255, 102)"/>
                        <option value="rgb(102, 185, 102)" label="rgb(102, 185, 102)"/>
                        <option value="rgb(102, 163, 224)" label="rgb(102, 163, 224)"/>
                        <option value="rgb(194, 133, 255)" label="rgb(194, 133, 255)"/>
                        <option value="rgb(136, 136, 136)" label="rgb(136, 136, 136)"/>
                        <option value="rgb(161, 0, 0)" label="rgb(161, 0, 0)"/>
                        <option value="rgb(178, 107, 0)" label="rgb(178, 107, 0)"/>
                        <option value="rgb(178, 178, 0)" label="rgb(178, 178, 0)"/>
                        <option value="rgb(0, 97, 0)" label="rgb(0, 97, 0)"/>
                        <option value="rgb(0, 71, 178)" label="rgb(0, 71, 178)"/>
                        <option value="rgb(107, 36, 178)" label="rgb(107, 36, 178)"/>
                        <option value="rgb(68, 68, 68)" label="rgb(68, 68, 68)"/>
                        <option value="rgb(92, 0, 0)" label="rgb(92, 0, 0)"/>
                        <option value="rgb(102, 61, 0)" label="rgb(102, 61, 0)"/>
                        <option value="rgb(102, 102, 0)" label="rgb(102, 102, 0)"/>
                        <option value="rgb(0, 55, 0)" label="rgb(0, 55, 0)"/>
                        <option value="rgb(0, 41, 102)" label="rgb(0, 41, 102)"/>
                        <option value="rgb(61, 20, 102)" label="rgb(61, 20, 102)"/>
                    </select>
                    <span className="ql-format-separator"/>
                    <select title="Background Color" className="ql-background">
                        <option value="rgb(0, 0, 0)" label="rgb(0, 0, 0)"/>
                        <option value="rgb(230, 0, 0)" label="rgb(230, 0, 0)"/>
                        <option value="rgb(255, 153, 0)" label="rgb(255, 153, 0)"/>
                        <option value="rgb(255, 255, 0)" label="rgb(255, 255, 0)"/>
                        <option value="rgb(0, 138, 0)" label="rgb(0, 138, 0)"/>
                        <option value="rgb(0, 102, 204)" label="rgb(0, 102, 204)"/>
                        <option value="rgb(153, 51, 255)" label="rgb(153, 51, 255)"/>
                        <option value="rgb(255, 255, 255)" label="rgb(255, 255, 255)"/>
                        <option value="rgb(250, 204, 204)" label="rgb(250, 204, 204)"/>
                        <option value="rgb(255, 235, 204)" label="rgb(255, 235, 204)"/>
                        <option value="rgb(255, 255, 204)" label="rgb(255, 255, 204)"/>
                        <option value="rgb(204, 232, 204)" label="rgb(204, 232, 204)"/>
                        <option value="rgb(204, 224, 245)" label="rgb(204, 224, 245)"/>
                        <option value="rgb(235, 214, 255)" label="rgb(235, 214, 255)"/>
                        <option value="rgb(187, 187, 187)" label="rgb(187, 187, 187)"/>
                        <option value="rgb(240, 102, 102)" label="rgb(240, 102, 102)"/>
                        <option value="rgb(255, 194, 102)" label="rgb(255, 194, 102)"/>
                        <option value="rgb(255, 255, 102)" label="rgb(255, 255, 102)"/>
                        <option value="rgb(102, 185, 102)" label="rgb(102, 185, 102)"/>
                        <option value="rgb(102, 163, 224)" label="rgb(102, 163, 224)"/>
                        <option value="rgb(194, 133, 255)" label="rgb(194, 133, 255)"/>
                        <option value="rgb(136, 136, 136)" label="rgb(136, 136, 136)"/>
                        <option value="rgb(161, 0, 0)" label="rgb(161, 0, 0)"/>
                        <option value="rgb(178, 107, 0)" label="rgb(178, 107, 0)"/>
                        <option value="rgb(178, 178, 0)" label="rgb(178, 178, 0)"/>
                        <option value="rgb(0, 97, 0)" label="rgb(0, 97, 0)"/>
                        <option value="rgb(0, 71, 178)" label="rgb(0, 71, 178)"/>
                        <option value="rgb(107, 36, 178)" label="rgb(107, 36, 178)"/>
                        <option value="rgb(68, 68, 68)" label="rgb(68, 68, 68)"/>
                        <option value="rgb(92, 0, 0)" label="rgb(92, 0, 0)"/>
                        <option value="rgb(102, 61, 0)" label="rgb(102, 61, 0)"/>
                        <option value="rgb(102, 102, 0)" label="rgb(102, 102, 0)"/>
                        <option value="rgb(0, 55, 0)" label="rgb(0, 55, 0)"/>
                        <option value="rgb(0, 41, 102)" label="rgb(0, 41, 102)"/>
                        <option value="rgb(61, 20, 102)" label="rgb(61, 20, 102)"/>
                    </select>
                    </span>
                    <span className="ql-format-group">
                    <span title="List" className="ql-format-button ql-list"/>
                    <span className="ql-format-separator"/>
                    <span title="Bullet" className="ql-format-button ql-bullet"/>
                    <span className="ql-format-separator"/>
                    <select title="Text Alignment" className="ql-align">
                        <option value="left" label="Left"/>
                        <option value="center" label="Center"/>
                        <option value="right" label="Right"/>
                        <option value="justify" label="Justify"/>
                    </select>
                    </span>
                </div>

                <div id="editor">
                    <div>Hello World!</div>
                    <div>Some initial <b>bold</b> text</div>
                    <div><br/></div>
                </div>
            </div>

        )
    }

    componentDidMount() {
        is_admin()
            .then(() => {

                this.setState({
                    loading: false
                })

                var that = this;
                var basicEditor = new Quill('#editor', {
                    theme: 'snow'
                });
                basicEditor.addModule('toolbar', {
                    container: '.toolbar'
                });
                basicEditor.on('text-change', function () {
                    var html = basicEditor.getHTML();
                    that.setState({
                        content: html
                    })
                });
            })
            .catch((err) => {
                document.location.href = "/";
            })
    }

    onSubmit() {
        const final_submission = {title: this.state.title, content: this.state.content};

        if (final_submission.title && final_submission.content) {
            this.setState({
                loading: true
            })
            create_post(final_submission.title, final_submission.content)
                .then((res) => {
                    this.setState({
                        loading: false
                    })
                });
        }
    }


    onChangeTitle(e) {
        this.setState({
            title: e.target.value
        })
    }


    render() {
        return (
            <div>
                {this.state.loading ? <div className="loader">Loading...</div> :
                    <div className="container text-center">
                        <div className="col-md-6 col-md-offset-3">

                            <h2>Title
                                <input type="text" className="form-control text-center"
                                       onChange={(e) => this.onChangeTitle(e)}/>
                            </h2>
                        </div>

                        <button type="button" className="btn btn-default" onClick={() => this.onSubmit()}>Submit
                        </button>

                        <div className="col-md-8 col-md-offset-2">

                            {this.editorConfig()}

                        </div>
                    </div>
                }
            </div>


        )
    }

}
