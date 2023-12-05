/* tslint:disable */
/* eslint-disable */
/**
 * kraken
 * The core component of kraken-project
 *
 * The version of the OpenAPI document: 0.1.0
 * Contact: git@omikron.dev
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * Request to resolve domains
 * @export
 * @interface DnsResolutionRequest
 */
export interface DnsResolutionRequest {
    /**
     * The leech to use
     * 
     * Leave empty to use a random leech
     * @type {string}
     * @memberof DnsResolutionRequest
     */
    leechUuid?: string | null;
    /**
     * The domains to resolve
     * @type {Array<string>}
     * @memberof DnsResolutionRequest
     */
    targets: Array<string>;
    /**
     * The concurrent task limit
     * @type {number}
     * @memberof DnsResolutionRequest
     */
    concurrentLimit: number;
    /**
     * The workspace to execute the attack in
     * @type {string}
     * @memberof DnsResolutionRequest
     */
    workspaceUuid: string;
}

/**
 * Check if a given object implements the DnsResolutionRequest interface.
 */
export function instanceOfDnsResolutionRequest(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "targets" in value;
    isInstance = isInstance && "concurrentLimit" in value;
    isInstance = isInstance && "workspaceUuid" in value;

    return isInstance;
}

export function DnsResolutionRequestFromJSON(json: any): DnsResolutionRequest {
    return DnsResolutionRequestFromJSONTyped(json, false);
}

export function DnsResolutionRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): DnsResolutionRequest {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'leechUuid': !exists(json, 'leech_uuid') ? undefined : json['leech_uuid'],
        'targets': json['targets'],
        'concurrentLimit': json['concurrent_limit'],
        'workspaceUuid': json['workspace_uuid'],
    };
}

export function DnsResolutionRequestToJSON(value?: DnsResolutionRequest | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'leech_uuid': value.leechUuid,
        'targets': value.targets,
        'concurrent_limit': value.concurrentLimit,
        'workspace_uuid': value.workspaceUuid,
    };
}

