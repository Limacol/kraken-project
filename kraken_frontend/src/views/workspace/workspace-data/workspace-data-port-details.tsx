import { Api } from "../../../api/api";
import React from "react";
import { FullHost, FullPort, TagType } from "../../../api/generated";
import { handleApiError } from "../../../utils/helper";
import Textarea from "../../../components/textarea";
import { toast } from "react-toastify";
import EditableTags from "../components/editable-tags";
import { WORKSPACE_CONTEXT } from "../workspace";

export type WorkspaceDataPortDetailsProps = {
    port: string;
    updatePort?: (uuid: string, update: Partial<FullPort>) => void;
    tab: "general" | "results" | "relations";
};

export function WorkspaceDataPortDetails(props: WorkspaceDataPortDetailsProps) {
    const { port: uuid, updatePort: signalUpdate, tab: tab } = props;
    const {
        workspace: { uuid: workspace },
    } = React.useContext(WORKSPACE_CONTEXT);

    const [port, setPort] = React.useState<FullPort | null>(null);
    React.useEffect(() => {
        Api.workspaces.ports.get(workspace, uuid).then(handleApiError(setPort));
    }, [workspace, uuid]);

    /** Send an update to the server and parent component */
    function update(uuid: string, update: Partial<FullPort>, msg?: string) {
        const { tags, comment } = update;
        Api.workspaces.ports
            .update(workspace, uuid, {
                comment,
                workspaceTags:
                    tags && tags.filter(({ tagType }) => tagType === TagType.Workspace).map(({ uuid }) => uuid),
                globalTags: tags && tags.filter(({ tagType }) => tagType === TagType.Global).map(({ uuid }) => uuid),
            })
            .then(
                handleApiError(() => {
                    if (msg !== undefined) toast.success(msg);
                    if (signalUpdate !== undefined) signalUpdate(uuid, update);
                })
            );
    }

    if (port === null) return null;
    return (
        <>
            {tab === "general" ? (
                <>
                    <div className={"pane"}>
                        <h3 className={"sub-heading"}>Port</h3>
                        {`${port.port} open on ${port.host.ipAddr}`}
                    </div>
                    <div className={"pane"}>
                        <h3 className={"sub-heading"}>Comment</h3>
                        <Textarea value={port.comment} onChange={(comment) => setPort({ ...port, comment })} />
                        <button
                            className={"button"}
                            onClick={() => port && update(port.uuid, { comment: port.comment }, "Updated comment")}
                        >
                            Update
                        </button>
                    </div>
                    <div className={"pane"}>
                        <h3 className={"sub-heading"}>Tags</h3>
                        <EditableTags
                            workspace={workspace}
                            tags={port.tags}
                            onChange={(tags) => {
                                setPort((port) => port && { ...port, tags });
                                update(port.uuid, { tags });
                            }}
                        />
                    </div>
                </>
            ) : (
                <>{tab === "results" ? <div> port results</div> : <div> port relations</div>}</>
            )}
        </>
    );
}
